import { BadRequestException, Body, Controller, HttpCode, Post, Req, type RawBodyRequest } from '@nestjs/common';
import type { Request } from 'express';
import { DigestService } from './digest.service';

export interface SyntheticEvent {
  event?: unknown;
}

export interface DigestReceipt {
  sha256: string;
  bytes: number;
  event: unknown;
}

// Mirrors the webhook shape later tasks need: digest the exact received bytes, not the re-serialized JSON.
@Controller('webhooks')
export class WebhookController {
  constructor(readonly digests: DigestService) {}

  @Post('synthetic')
  @HttpCode(200)
  receive(@Req() req: RawBodyRequest<Request>, @Body() body: SyntheticEvent): DigestReceipt {
    if (!req.rawBody) throw new BadRequestException('raw body unavailable');
    return { sha256: this.digests.sha256(req.rawBody), bytes: req.rawBody.length, event: body.event };
  }
}
