import { Module } from '@nestjs/common';
import { DigestService } from './digest.service';
import { WebhookController } from './webhook.controller';

@Module({
  controllers: [WebhookController],
  providers: [DigestService],
})
export class AppModule {}
