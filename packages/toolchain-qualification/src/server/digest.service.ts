import { createHash } from 'node:crypto';
import { Injectable } from '@nestjs/common';

@Injectable()
export class DigestService {
  sha256(bytes: Buffer): string {
    return createHash('sha256').update(bytes).digest('hex');
  }
}
